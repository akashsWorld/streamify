import { Component } from '@angular/core';
import { InputComponent } from '../../components/input/input.component';
import { ButtonComponent } from '../../components/button/button.component';
import { Router } from '@angular/router';
import { faEye,faEyeSlash } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [InputComponent,ButtonComponent,FontAwesomeModule],
  templateUrl: './sign-up.component.html'
})
export class SignUpComponent {

  passwordVisible=faEye
  passwordNotVisible = faEyeSlash

  constructor(protected router:Router){}

  showPassword=true
  
  showConfirmPassword = true


}
