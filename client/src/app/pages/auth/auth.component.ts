import { NgOptimizedImage } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserService } from '../../service/user.service';
@Component({
  selector: 'app-auth',
  standalone: true,
  providers:[UserService],
  imports: [RouterOutlet,NgOptimizedImage],
  templateUrl: './auth.component.html'
})
export class AuthComponent {

}
