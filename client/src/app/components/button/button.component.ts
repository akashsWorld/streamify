import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [],
  templateUrl: './button.component.html',
  styleUrl: './button.component.css'
})
export class ButtonComponent {

  @Input({required:true})
  buttonName =''

  @Input({required:false})
  buttonType:'primary'|'secondary' ='primary'


}
