import { Component, OnInit } from '@angular/core';
import { faEye,faEyeSlash } from '@fortawesome/free-regular-svg-icons';
import { InputComponent } from '../../components/input/input.component';
import { Router } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FormsModule } from '@angular/forms';
import { UserService } from '../../service/user.service';
import { NgClass } from '@angular/common';
@Component({
  selector: 'app-sign-in',
  standalone: true,
  imports: [InputComponent,FontAwesomeModule,FormsModule,NgClass],
  templateUrl: './sign-in.component.html'
})
export class SignInComponent {

  passwordVisible=faEye
  passwordNotVisible=faEyeSlash

  error = false
  userLogin={
    email:'',
    password:''
  }

  constructor(protected router:Router,protected userService:UserService){}

  onLogin(){
    if(this.userLogin.email.includes('@') && this.userLogin.password.length>=8){
      this.userService.loginUser(this.userLogin).subscribe(res=>{
        if(res.status==200){
          const {user_name,first_name,last_name,token,channel_name} = res.body
          this.userService.userToken.set(token)
          this.userService.userDetails.set({
            firstName:first_name,
            lastName:last_name,
            userName:user_name,
            channelName:channel_name
          })
          this.router.navigateByUrl('/')
        }
      })
    }else{
      this.error=true;
    }
  }


  showPassword=false
  
}
