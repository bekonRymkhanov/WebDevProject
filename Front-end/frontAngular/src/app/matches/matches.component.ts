import {Component, OnInit} from '@angular/core';
import {Match} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {NgForOf, NgIf} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {RouterLink} from "@angular/router";
import {retry} from "rxjs";

@Component({
  selector: 'app-matches',
  standalone: true,
  imports: [
    NgIf,
    FormsModule,
    NgForOf,
    RouterLink
  ],
  templateUrl: './matches.component.html',
  styleUrl: './matches.component.css'
})
export class MatchesComponent implements OnInit{
  matches!:Match[];
  loaded:boolean=false
  newMatch:Match;



  constructor(private httpService:OneXBetService)  {
    this.newMatch = {
      "id":0,
      "match_date":'',
      "state1": 0,
      "state2": 0,
      "state3": 0,
      "home_club": {
        "id":0,
        "name":'',
        "points":0
      },
      "away_club": {
        "id":0,
        "name":'',
        "points":0
      }
    }

  }

  ngOnInit(): void {
    this.getMatches()
    const access=localStorage.getItem('access');
    if(access){
      this.loaded=true;
      this.getMatches()
    }
  }
  getMatches(){
    this.loaded=false;
    this.httpService.getMatches().subscribe(matches=>this.matches=matches);
    this.loaded=true;
  }
  DeleteMatches(id :number){
    this.httpService.deleteMatch(id).subscribe(()=>{
      this.matches = this.matches.filter(match => match.id !== id);
    })
  }
  CreateMatch(){
    const maxId = Math.max(...this.matches.map(match => match.id), 0);
    var copy: Match = {
      id: maxId + 1,
      match_date:new Date().toISOString(),
      state1: this.newMatch.state1,
      state2: this.newMatch.state2,
      state3: this.newMatch.state3,
      home_club: {
        id:0,
        name:'',
        points:0
      },
      away_club: {
        id:0,
        name:'',
        points:0
      }
    };
    this.httpService.getClub(this.newMatch.away_club.id).subscribe(club=>{
      copy.away_club=club
    })
    this.httpService.getClub(this.newMatch.home_club.id).subscribe(club => {
      copy.home_club = club;
      this.httpService.postMatch(copy).subscribe((match) => {
        this.matches.unshift(match);

        this.newMatch.match_date = '';
        this.newMatch.state1 =0;
        this.newMatch.state2 =0;
        this.newMatch.state3 =0;

        this.newMatch.home_club = {
          id:0,
          name:'',
          points:0,
        };
        this.newMatch.away_club = {
          id:0,
          name:'',
          points:0,
        };
      });
    });
  }



}
