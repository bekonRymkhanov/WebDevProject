import { Component } from '@angular/core';
import {NgForOf, NgIf} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {RouterLink} from "@angular/router";
import {Club} from "../models";
import {OneXBetService} from "../one-xbet.service";

@Component({
  selector: 'app-clubs',
  standalone: true,
  imports: [
    NgIf,
    FormsModule,
    RouterLink,
    NgForOf
  ],
  templateUrl: './clubs.component.html',
  styleUrl: './clubs.component.css'
})
export class ClubsComponent {
  clubs!:Club[];
  loaded:boolean=false
  newClub:Club;
  logged:boolean=false;

  constructor(private httpService:OneXBetService)  {
    this.newClub = {
      "id":0,
      "name":"",
      "points":0
    }

  }

  ngOnInit(): void {
    this.getClubs()
    const access=localStorage.getItem('access');
    if(access){
      this.logged=true;
      this.getClubs()
    }
  }
  getClubs(){
    this.loaded=false;
    this.httpService.getTopTenClubs().subscribe(clubs=>this.clubs=clubs);
    this.loaded=true;
  }
  DeleteClub(id :number){
    this.httpService.deleteClub(id).subscribe(()=>{  this.clubs = this.clubs.filter(club => club.id !== id);
    })
  }
  CreateClub(){
    const maxId = Math.max(...this.clubs.map(club => club.id), 0);
    var copy:Club={
      id:maxId+1,
      name:this.newClub.name,
      points:this.newClub.points
    };

    this.httpService.postClub(this.newClub).subscribe((club)=>    this.clubs.unshift(club))
    this.newClub.name='';
    this.newClub.points=0;

  }




}

