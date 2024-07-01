import { NgOptimizedImage } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [RouterOutlet,NgOptimizedImage],
  templateUrl: './auth.component.html'
})
export class AuthComponent {

}
