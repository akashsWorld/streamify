import { HttpClient } from '@angular/common/http';
import {
    Inject,
  Injectable,
  signal,
  WritableSignal,
} from '@angular/core';
import { Observable } from 'rxjs';
import { BrowserStorageService } from './browser.service';

export interface UserObejct {
  first_name?: string;
  last_name?: string;
  email?: string;
  user_name?: string;
  password?: string;
}
export interface UserLogin {
  email: string;
  password: string;
}

@Injectable({
  providedIn: 'root',
})
export class UserService {
 userToken: WritableSignal<string|null> = signal(null);

 userDetails:WritableSignal<{firstName?:string,lastName?:string,userName?:string,channelName:string}|null>=signal(null)

 constructor(
    private http: HttpClient,
    private browserService: BrowserStorageService
  ) {
    const userToken = browserService.get('user-token');
    if (userToken) {
      this.userToken.set(userToken)
    }
  }

  setUserToken(token:string){
    this.userToken.set(token) 
    this.browserService.set('user-token',token)
  }

  logoutUser(){
    this.userToken.set(null) 
    this.browserService.delete('user-token')
  }

  createUser(user: UserObejct): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/user/', user, {
      observe: 'response',
    });
  }

  loginUser(user: UserLogin): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/user/auth/', user, {
      observe: 'response',
    });
  }

  updateUser(user: UserObejct) {
    return this.http.put('http://127.0.0.1:8000/user/', user, {
      observe: 'response',
    });
  }

  commentVideo() {}

  likeVideo() {}
}
