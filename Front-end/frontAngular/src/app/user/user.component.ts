import {Component, OnInit} from '@angular/core';
import {MyUser} from "../models";
import {OneXBetService} from "../one-xbet.service";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [
    NgIf
  ],
  templateUrl: './user.component.html',
  styleUrl: './user.component.css'
})
export class UserComponent implements OnInit{
  loaded:boolean=false
  newUser:MyUser;

  ngOnInit(): void {
    this.httpService.getUsers().subscribe(data=>{
      this.loaded=false;
      this.newUser=data[0]
      this.loaded=true;
    })
  }
  constructor(private httpService:OneXBetService) {
    this.newUser={
      "id":0,
      "name":'',
      "email":'',
      "password":'',
      "balance":0,
    }
  }
}
