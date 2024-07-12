import { Component, OnChanges, SimpleChanges } from '@angular/core';
import { InputComponent } from '../../components/input/input.component';
import { ButtonComponent } from '../../components/button/button.component';
import { Router } from '@angular/router';
import { faEye,faEyeSlash } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UserObejct, UserService } from '../../service/user.service';
import { FormsModule } from '@angular/forms';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [InputComponent,ButtonComponent,FontAwesomeModule,FormsModule,NgClass],
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

  showPassword=false
  
  showConfirmPassword = true

  confirmPassword = ''

  isPasswordMatches = false

  error=false

  onChangePassword(eve:string){
    this.newUser.password = eve
    if(this.confirmPassword!==this.newUser.password){
      this.error=true
    }else{
      this.error=false
    }
  }

  onChangeConfirmPassword(eve:Event): void {
    // console.log('Hello World')
    this.confirmPassword = (eve.target as HTMLInputElement).value
    if(this.confirmPassword!==this.newUser.password){
      this.error=true
    }else{
      this.error=false
    }
  }

  onCrateUser(){
    const userObservable = this.userService.createUser(this.newUser)
    userObservable.subscribe((res)=>{
      if(res.status!==201){
        this.router.navigateByUrl('/error-occured')
      }else{
        this.router.navigateByUrl('/auth')
      }
    })
  }
  

}
