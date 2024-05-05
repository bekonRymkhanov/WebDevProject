import {Component, OnInit} from '@angular/core';
import {FormsModule} from "@angular/forms";
import {Bet, Match} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {ActivatedRoute, RouterLink} from "@angular/router";
import {NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-match-details',
  standalone: true,
  imports: [
    FormsModule,
    NgIf,
    NgForOf,
    RouterLink
  ],
  templateUrl: './match-details.component.html',
  styleUrl: './match-details.component.css'
})
export class MatchDetailsComponent implements OnInit{
  match!:Match;
  loaded:boolean=false;
  newBet:Bet;
  bets!:Bet[];

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
      const matchId = params['matchId'];
      this.httpService.getMatch(matchId).subscribe(match => {
        this.match = match;
        console.log(match)
        this.loaded=false;
        this.httpService.getBets().subscribe(bets=>this.bets=bets);
        this.loaded=true;

      });
    });
  }

  DeleteBet(id :number){
    this.httpService.deleteBet(id).subscribe(()=>{  this.bets = this.bets.filter(bet => bet.id !== id);
    })
  }
  CreateBets() {
    const maxId = Math.max(...this.bets.map(bet => bet.id), 0);
    var copy: Bet = {
      id: maxId + 1,
      match: this.match.id,
      state_chosen: this.newBet.state_chosen,
      amount:this.newBet.amount,
      user:0
    };
    this.httpService.getUsers().subscribe(user=>{
      if (user[0].balance<parseInt(this.newBet.amount)){
        return ;
      }

      user[0].balance-=parseInt(this.newBet.amount)
      this.httpService.putUser(user[0]).subscribe(user=>{
        copy.user=user.id
        this.httpService.postBet(copy).subscribe((bet) => {
          this.bets.unshift(bet);

          this.newBet.state_chosen=0;
          this.newBet.amount='';
        })
      })




    });
  }
}
