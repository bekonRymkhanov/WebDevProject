import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {Bet, Match} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-bets',
  standalone: true,
  imports: [
    FormsModule,
    NgForOf,
    NgIf,
    RouterLink
  ],
  templateUrl: './bets.component.html',
  styleUrl: './bets.component.css'
})
export class BetsComponent {
  bets!:Bet[];
  loaded:boolean=false

  constructor(private httpService:OneXBetService)  {
  }

  ngOnInit(): void {
    this.getBets()
    const access=localStorage.getItem('access');
    if(access){
      this.loaded=true;
      this.getBets()
    }
  }
  getBets(){
    this.loaded=false;
    this.httpService.getBets().subscribe(bets=>this.bets=bets);
    this.loaded=true;
  }
  DeleteBet(id :number){
    this.httpService.deleteBet(id).subscribe(()=>{
      this.bets = this.bets.filter(bet => bet.id !== id);
    })
  }



}
