import { Component } from '@angular/core';
import { faEye,faEyeSlash } from '@fortawesome/free-regular-svg-icons';
import { InputComponent } from '../../components/input/input.component';
import { Router } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
@Component({
  selector: 'app-sign-in',
  standalone: true,
  imports: [InputComponent,FontAwesomeModule],
  templateUrl: './sign-in.component.html'
})
export class SignInComponent {

  passwordVisible=faEye
  passwordNotVisible=faEyeSlash

  constructor(protected router:Router){}

  showPassword=false
}
