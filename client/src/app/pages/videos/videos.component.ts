import { Component,ViewChild,ElementRef } from '@angular/core';

@Component({
  selector: 'app-videos',
  standalone: true,
  imports: [],
  templateUrl: './videos.component.html'
})
export class VideosComponent {
  @ViewChild('billBoard', { static: false }) billBoard: ElementRef|undefined= undefined;

  playVideo() {
    console.log('Hello ')
    console.log(this.billBoard)
    if(this.billBoard)
    this.billBoard.nativeElement.play();
  }
}
