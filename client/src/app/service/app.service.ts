import { Injectable, signal } from "@angular/core";

export interface UserResponse {
    firstName: string;
    lastName: string;
    userName: string;
    channelName: string|null;
}

@Injectable({
    providedIn:'root'
})
export class AppService{

    userToken = signal<string|null>(null);

    userDetails = signal<UserResponse|null>(null);

}