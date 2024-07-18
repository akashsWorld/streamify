import {ChangeDetectionStrategy, Component, computed, EventEmitter, Input, Output} from '@angular/core';
import {NgOptimizedImage} from "@angular/common";
import { NavigationEnd, Route, Router, RouterModule, RouterState } from '@angular/router';
import {ButtonComponent} from "../button/button.component";
import {FormsModule} from "@angular/forms";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {faUser} from '@fortawesome/free-regular-svg-icons'
import {faVideo} from '@fortawesome/free-solid-svg-icons'
import { UserService } from '../../service/user.service';
import { AppService } from '../../service/app.service';
@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    NgOptimizedImage,
    FormsModule,
    ButtonComponent,
    FontAwesomeModule
  ],
  templateUrl: './navbar.component.html',
  changeDetection:ChangeDetectionStrategy.OnPush
})
export class NavbarComponent {


  userIcon = faUser
  VideoIcon = faVideo

  searchString:string=''

  isLoggedIn=computed<string|null>(()=>{
    const user = this.appService.userDetails()
    console.log('Executed')
    if(user){
      console.log("Hello World");
      return `${user.firstName} ${user.lastName}`
    }
    return null
  })


  haveAnyChannel = computed<string|null>(()=>{
    const user = this.appService.userDetails()
    if(user)
      return user.channelName
    return null;
  })

  @Output()
  onSearch = new EventEmitter<string>()

  onEnterSearch=()=>{
    console.log('Key pressed');
    this.onSearch.emit()
  }

  currentUrl = ''
  constructor(protected router:Router,public userService:UserService,private appService:AppService){}
  
  
  ngOnInit(): void {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.currentUrl = event.url
      }
    }); 
  }

}
