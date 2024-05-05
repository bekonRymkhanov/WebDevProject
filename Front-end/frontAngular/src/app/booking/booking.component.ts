import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-booking',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './booking.component.html',
  styleUrl: './booking.component.css'
})
export class BookingComponent {
  // Avilable!:String[]=["A1","A3","C1","C2","D2","D3","D4","D5"]
  NumberChosen:Number=0
  // slotnumber:String=''
  confirm(){

  }


}
