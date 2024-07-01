import {Component, EventEmitter, Input, Output} from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [],
  template: '<button (click)="onClickHandle()" class="btn">{{buttonName}}</button>'
})
export class ButtonComponent {

  @Input({required:true})
  buttonName =''

  @Input({required:false})
  buttonType:'primary'|'secondary' ='primary'

  @Output()
  click = new EventEmitter<void>()

  onClickHandle(){
    this.click.emit()
  }


}
