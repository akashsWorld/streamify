import { NgClass } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { ValueChangeEvent } from '@angular/forms';

@Component({
  selector: 'app-input',
  standalone: true,
  imports: [NgClass],
  templateUrl:'./input.component.html' 
})
export class InputComponent {
  @Input()
  type = '';

  @Input()
  name = '';

  @Input({required:false})
  error=false

  @Input({alias:'class',required:false})
  style=''

  @Output()
  inputValue = new EventEmitter<string>();

  onChange(eve: Event) {
    this.inputValue.emit((eve.target as HTMLInputElement).value)
  }
}
