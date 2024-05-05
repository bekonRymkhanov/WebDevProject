import { Routes } from '@angular/router';
import { ClubsComponent } from './clubs/clubs.component';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import {MatchesComponent} from "./matches/matches.component";
import {UserComponent} from "./user/user.component";
import {MatchesByClubsComponent} from "./matches-by-clubs/matches-by-clubs.component";
import {MatchDetailsComponent} from "./match-details/match-details.component";
import {BetsComponent} from "./bets/bets.component";
import {BetDetailsComponent} from "./bet-details/bet-details.component";
import {BookingComponent} from "./booking/booking.component";

export const routes: Routes = [
    { path:"",redirectTo:"home",pathMatch:"full" },
    { path:"home",component:HomeComponent,title:"Home page" },
    { path:"about",component:AboutComponent,title:"About page" },
    { path:"clubs",component:ClubsComponent,title:"clubs page" },
    { path:"matches",component:MatchesComponent,title:"matches page" },
    { path:"matches/:matchId",component:MatchDetailsComponent,title:"match details page" },
    { path:"bets",component:BetsComponent,title:"bets page" },
    { path:"bets/:betId",component:BetDetailsComponent,title:"bets detail page" },
    { path:"booking",component:BookingComponent,title:"booking of place"},
    { path:"user_detail",component:UserComponent,title:"profile page" },

    { path:"clubs/:clubId/matches", component:MatchesByClubsComponent,
      title:"matches of club page" },
    { path:"**",component:NotFoundComponent,title:"404 - not found" }
];
