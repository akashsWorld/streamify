import {Component, EventEmitter, Input, Output} from '@angular/core';
import {NgOptimizedImage} from "@angular/common";
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
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  userIcon = faUser
  VideoIcon = faVideo
  searchString:string=''

  @Input()
  isLoggedIn=false

  @Input({required:false})
  haveAnyChannel:null|string = 'Tech Barney'

  @Output()
  onSearch = new EventEmitter<string>()

  onEnterSearch=()=>{
    console.log('Key pressed');
    this.onSearch.emit()
  }

  

}
