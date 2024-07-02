import { Component } from '@angular/core';
import { InputComponent } from '../../components/input/input.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { NgOptimizedImage } from '@angular/common';
@Component({
  selector: 'app-create-channel',
  standalone: true,
  imports: [InputComponent,FontAwesomeModule,NgOptimizedImage],
  templateUrl: './create-channel.component.html'
})
export class CreateChannelComponent  {
  
  faUser = faUser

  channelIcon:string|null =''

}
