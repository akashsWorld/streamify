import {Component, EventEmitter, Input, Output} from '@angular/core';
import {NgOptimizedImage} from "@angular/common";
import { Route, Router, RouterModule } from '@angular/router';
import {ButtonComponent} from "../button/button.component";
import {FormsModule} from "@angular/forms";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {faUser} from '@fortawesome/free-regular-svg-icons'
import {faVideo} from '@fortawesome/free-solid-svg-icons'
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

  constructor(protected router:Router){}

  userIcon = faUser
  VideoIcon = faVideo
  searchString:string=''

  @Input()
  isLoggedIn=true

  @Input({required:false})
  haveAnyChannel:null|string = null

  @Output()
  onSearch = new EventEmitter<string>()

  onEnterSearch=()=>{
    console.log('Key pressed');
    this.onSearch.emit()
    
  }  

}
