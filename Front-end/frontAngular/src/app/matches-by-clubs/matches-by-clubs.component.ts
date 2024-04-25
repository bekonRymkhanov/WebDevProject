import {Component, OnInit} from '@angular/core';
import {Club, Match} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {ActivatedRoute, RouterLink} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {log} from "@angular-devkit/build-angular/src/builders/ssr-dev-server";

@Component({
  selector: 'app-matches-by-clubs',
  standalone: true,
  imports: [
    FormsModule,
    NgIf,
    NgForOf,
    RouterLink
  ],
  templateUrl: './matches-by-clubs.component.html',
  styleUrl: './matches-by-clubs.component.css'
})
export class MatchesByClubsComponent implements OnInit{
  matches!: Match[];
  club!: Club;
  loaded: boolean = false;
  newMatch: Match;

  constructor(private httpService:OneXBetService, private route: ActivatedRoute) {
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
    };
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const clubId = params['clubId'];
      this.httpService.getClub(clubId).subscribe(club => {
        this.club = club;
        this.newMatch.home_club = this.club;
        this.getMatchesByClubs(this.club.id);

      });
    });
  }

  getMatchesByClubs(id: number) {
    this.loaded = false;
    this.httpService.getMatchesByClub(id).subscribe(matches => {
      this.matches = matches;
      this.loaded = true;
    });
  }

  DeleteMatch(id: number) {
    this.httpService.deleteMatch(id).subscribe(() => {
      this.matches = this.matches.filter(match => match.id !== id);
    });
  }

  CreateMatch() {
    this.httpService.getMatches().subscribe(matches => {
      const maxId = Math.max(...matches.map(match => match.id), 0);
      const copy: Match = {
        id: maxId + 1,
        match_date:new Date().toISOString(),
        state1: this.newMatch.state1,
        state2: this.newMatch.state2,
        state3: this.newMatch.state3,
        home_club: this.club,
        away_club: {
          id:0,
          name:'',
          points:0
        }
      };
      this.httpService.getClub(this.newMatch.away_club.id).subscribe(club=>{
        copy.away_club=club
        this.httpService.postMatch(copy).subscribe((match) => {
          this.matches.unshift(match);

          this.newMatch.match_date = '';
          this.newMatch.state1 =0;
          this.newMatch.state2 =0;
          this.newMatch.state3 =0;
          this.newMatch.away_club = {
            id:0,
            name:'',
            points:0,
          };
        });
      })


    });
  }
}

