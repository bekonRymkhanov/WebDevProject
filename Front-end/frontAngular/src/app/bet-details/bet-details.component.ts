import {Component, OnInit} from '@angular/core';
import {FormsModule} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {Bet, Match} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {ActivatedRoute, RouterLink} from "@angular/router";

@Component({
  selector: 'app-bet-details',
  standalone: true,
  imports: [
    FormsModule,
    NgForOf,
    NgIf,
    RouterLink
  ],
  templateUrl: './bet-details.component.html',
  styleUrl: './bet-details.component.css'
})
export class BetDetailsComponent implements OnInit{
  bet!:Bet;
  loaded:boolean=false;
  newBet:Bet;

  constructor(private httpService:OneXBetService,private route: ActivatedRoute) {
    this.newBet = {
      "id":0,
      "match": 0,
      "state_chosen": 0,
      "amount":'',
      "user": 0
    }
  }
  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.loaded=false;
      const betId = params['betId'];
      this.httpService.getBet(betId).subscribe(bet => {
        this.bet =bet;
        this.newBet.state_chosen=bet.state_chosen;
        this.newBet.amount=bet.amount;

        this.loaded=true;

      });
    });
  }

  DeleteBet(id :number){
    this.httpService.deleteBet(id).subscribe();
  }
  UpdateBets() {

    var copy: Bet = {
      id: this.bet.id,
      match: this.bet.match,
      state_chosen: this.newBet.state_chosen,
      amount:this.newBet.amount,
      user:this.bet.user
    };

    this.httpService.putBet(copy).subscribe((bet) => {
      this.bet=bet;
    })



  }
}
