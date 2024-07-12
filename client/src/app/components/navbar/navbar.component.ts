import {Component, computed, EventEmitter, Input, Output} from '@angular/core';
import {NgOptimizedImage} from "@angular/common";
import { NavigationEnd, Route, Router, RouterModule, RouterState } from '@angular/router';
import {ButtonComponent} from "../button/button.component";
import {FormsModule} from "@angular/forms";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {faUser} from '@fortawesome/free-regular-svg-icons'
import {faVideo} from '@fortawesome/free-solid-svg-icons'
import { UserService } from '../../service/user.service';
@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    NgOptimizedImage,
    FormsModule,
    ButtonComponent,
    FontAwesomeModule
  ],
  templateUrl: './navbar.component.html'
})
export class NavbarComponent {


  userIcon = faUser
  VideoIcon = faVideo

  searchString:string=''

  isLoggedIn=computed<string|null>(()=>{
    const user = this.userService.userDetails()
    console.log('Executed')
    if(user)
      return `${user.firstName} ${user.lastName}`
    return null
  })


  haveAnyChannel = computed<string|null>(()=>{
    const user = this.userService.userDetails()
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
  constructor(protected router:Router,protected userService:UserService){}

  
  ngOnInit(): void {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.currentUrl = event.url
      }
    }); 
  }

}
