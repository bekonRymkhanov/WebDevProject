import {Component, OnInit} from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import { ClubsComponent } from './clubs/clubs.component';
import { CommonModule } from '@angular/common';
import {BetDetailsComponent} from "./bet-details/bet-details.component";
import {BetsComponent} from "./bets/bets.component";
import {MatchesComponent} from "./matches/matches.component";
import {MatchDetailsComponent} from "./match-details/match-details.component";
import {MatchesByClubsComponent} from "./matches-by-clubs/matches-by-clubs.component";
import {UserComponent} from "./user/user.component";
import {FormsModule} from "@angular/forms";
import {OneXBetService} from "./one-xbet.service";
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ClubsComponent, CommonModule, BetDetailsComponent, BetsComponent, MatchesComponent, MatchDetailsComponent, MatchesByClubsComponent, UserComponent, RouterLink, FormsModule,HomeComponent,AboutComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit{
  constructor(private httpService:OneXBetService) {
  }

  ngOnInit(): void {
  }
  logged:boolean=false;
  title = '1x-bet';
  email :string='';
  password:string='';
  balance:number=0;
  name:string='';
  login(){
    return this.httpService.login(this.email,this.password).subscribe(data=>{
      this.logged=true;
      localStorage.setItem("access",data.access)
      localStorage.setItem("refresh",data.refresh)
      this.name='';
      this.email='';
      this.password='';
      this.name='';
      this.balance=0;

    })

  }
  reqister(){
    return this.httpService.register(this.name,this.email,this.password,this.balance).subscribe(data=>this.login())
  }

  logout(){
    this.logged=false;
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")

  }


  protected readonly localStorage = localStorage;
}
