import { Component, EventEmitter, Input, Output } from '@angular/core';
import { ValueChangeEvent } from '@angular/forms';

@Component({
  selector: 'app-input',
  standalone: true,
  imports: [],
  template: `
    <label for="some-input" class="text-primaryWhite font-semibold text-lg mx-4 p-3 min-h-9">
      {{ name+' :' }}
      <input
        class="outline-none rounded-md bg-transparent text-white border font-body h-9 mx-3 max-w-8/12 p-3"
        name="some-input"
        type="{{ type }}"
        (change)="onChange($event)"
      />
    </label>
  `
})
export class InputComponent {
  @Input()
  type = '';

  @Input()
  name = '';

  @Input({alias:'class',required:false})
  style=''

  @Output()
  change = new EventEmitter<string>();


  onChange(eve: Event) {
    console.log((eve.target as HTMLInputElement).value);
  }
}
