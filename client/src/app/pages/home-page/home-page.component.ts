import { Component } from '@angular/core';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { RouterModule } from '@angular/router';
@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [NavbarComponent,RouterModule],
  templateUrl: './home-page.component.html'
})
export class HomePageComponent {
  
  

}
