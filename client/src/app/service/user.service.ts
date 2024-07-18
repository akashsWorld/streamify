import { HttpClient } from '@angular/common/http';
import { Inject, Injectable, signal, WritableSignal } from '@angular/core';
import { Observable } from 'rxjs';
import { BrowserStorageService } from './browser.service';
import { AppService } from './app.service';

export interface UserObejct {
  first_name: string;
  last_name: string;
  email: string;
  user_name: string;
  password: string;
}
export interface UserLogin {
  email: string;
  password: string;
}

export interface UserResponse {
  firstName: string;
  lastName: string;
  userName: string;
  channelName: string|null;
}


@Injectable({
  providedIn: 'root',
})
export class UserService {

  
  constructor(
    private http: HttpClient,
    private browserService: BrowserStorageService,
    private appService:AppService
  ) {
    const userToken = browserService.get('user-token');
    if (userToken) {
      this.appService.userToken.set(userToken);
      const headers = {
        Authorization:`Bearer ${userToken}`
      }
        http.get<any>('http://localhost:8000/user/auth',{observe:'response',headers}).subscribe(res=>{
            if(res.status===200){
                const {user_name,first_name,last_name,channel_name} = res.body
                this.appService.userDetails.set({
                    firstName: first_name,
                    lastName:last_name,
                    userName:user_name,
                    channelName:channel_name
                })
            }else{
                browserService.delete('user-token')
            }
        })

    }
  }

  setUserToken(token: string) {
    this.appService.userToken.set(token);
    this.browserService.set('user-token', token);
  }

  logoutUser() {
    this.appService.userToken.set(null);
    this.browserService.delete('user-token');
  }

  createUser(user: UserObejct): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/user/', user, {
      observe: 'response',
    });
  }

  loginUser(user: UserLogin): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/user/login/', user, {
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
