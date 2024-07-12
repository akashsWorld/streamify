import { Injectable, signal, WritableSignal } from "@angular/core";


@Injectable({
    providedIn:'root'
})
export class AppService{

    userToken:WritableSignal<string>=signal('')
}