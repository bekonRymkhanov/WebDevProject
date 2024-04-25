import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Bet, Club, Match, MyUser, Token} from "./models";

@Injectable({
  providedIn: 'root'
})
export class OneXBetService {

  constructor(private client:HttpClient) { }
  getClubs(){
    return this.client.get<Club[]>(`http://127.0.0.1:8000/api/clubs/`,)
  }
  getClub(id:number){
    return this.client.get<Club>(`http://127.0.0.1:8000/api/clubs/${id}/`)
  }
  deleteClub(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/clubs/${id}/`)
  }
  postClub(newClub:Club){
    console.log(newClub.id)

    return this.client.post<Club>(`http://127.0.0.1:8000/api/clubs/`,newClub)
  }
  putClub(newClub:Club){
    return this.client.put<Club>(`http://127.0.0.1:8000/api/clubs/${newClub.id}/`,newClub)
  }

  getMatchesByClub(clubId: number) {
    return this.client.get<Match[]>(`http://127.0.0.1:8000/api/clubs/${clubId}/matches/`)
  }
  getMatches(){
    return this.client.get<Match[]>(`http://127.0.0.1:8000/api/matches/`,)
  }
  getMatch(id:number){
    return this.client.get<Match>(`http://127.0.0.1:8000/api/matches/${id}/`)
  }
  deleteMatch(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/matches/${id}/`)
  }
  postMatch(newMatch:Match){
    return this.client.post<Match>(`http://127.0.0.1:8000/api/matches/`,newMatch)
  }
  putMatch(newMatch:Match){
    return this.client.put<Match>(`http://127.0.0.1:8000/api/matches/${newMatch.id}/`,newMatch)
  }
  getTopTenClubs(){
    return this.client.get<Club[]>(`http://127.0.0.1:8000/api/clubs/top_20/`)
  }
  login(email:string,password:string){
    return this.client.post<Token>(`http://127.0.0.1:8000/api/login/`,{email,password})
  }
  register(name:string,email:string,password:string,balance:number){
    return this.client.post<MyUser>(`http://127.0.0.1:8000/api/register/`,{name,email,password,balance})
  }

  getUsers(){
    return this.client.get<MyUser[]>(`http://127.0.0.1:8000/api/users/`,)
  }
  getUser(id:number){
    return this.client.get<MyUser>(`http://127.0.0.1:8000/api/users/${id}/`)
  }
  deleteUser(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/users/${id}/`)
  }
  putUser(newUser:MyUser){
    return this.client.put<MyUser>(`http://127.0.0.1:8000/api/users/${newUser.id}/`,newUser)
  }
  getBets(){
    return this.client.get<Bet[]>(`http://127.0.0.1:8000/api/bets/`)
  }
  deleteBet(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/bets/${id}/`)
  }
  postBet(newBet:Bet){
    return this.client.post<Bet>(`http://127.0.0.1:8000/api/bets/`,newBet)
  }
  getBet(id:number){
    return this.client.get<Bet>(`http://127.0.0.1:8000/api/bets/${id}`)
  }
  putBet(newBet:Bet){
    return this.client.put<Bet>(`http://127.0.0.1:8000/api/bets/${newBet.id}/`,newBet)
  }
}

