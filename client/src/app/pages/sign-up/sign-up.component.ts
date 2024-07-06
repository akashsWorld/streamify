import { Component } from '@angular/core';
import { InputComponent } from '../../components/input/input.component';
import { ButtonComponent } from '../../components/button/button.component';
import { Router } from '@angular/router';
import { faEye,faEyeSlash } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UserObejct, UserService } from '../../service/user.service';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [InputComponent,ButtonComponent,FontAwesomeModule],
  templateUrl: './sign-up.component.html'
})
export class SignUpComponent {

  passwordVisible=faEye
  passwordNotVisible = faEyeSlash


  newUser:UserObejct = {
    first_name : '',
    last_name :'',
    email:'',
    user_name:'',
    password:''
  }

  constructor(protected router:Router,private userService:UserService){}

  showPassword=true
  
  showConfirmPassword = true

  confirmPassword = ''

  isPasswordMatches = false

  onCrateUser(){
    const userObservable = this.userService.createUser(this.newUser)
    userObservable.subscribe((res)=>{
      if(res.status===201){
        // Update the Login user. 
      }
      this.router.navigateByUrl('')
    })
  }

}
