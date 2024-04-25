export interface Club{
  "id":number,
  "name":string,
  "points":number
}
export interface Match{
  "id":number,
  "home_club":Club,
  "away_club":Club,
  "match_date":string,
  "state1":number,
  "state2":number,
  "state3":number,
}

export interface MyUser{
  "id":number,
  "balance":number,
  "email":string,
  "password":string,
  "name":string
}
export interface Bet{
  "id":number,
  "match": number,
  "state_chosen": number,
  "amount":string,
  "user": number
}
export interface Token{
  access:string,
  refresh:string,
}

