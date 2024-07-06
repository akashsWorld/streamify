import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

export interface UserObejct{
    first_name:string,
    last_name:string,
    email:string,
    user_name:string,
    password:string
}

@Injectable()
export class UserService{

    constructor(private http:HttpClient){}

    createUser (user:UserObejct) :Observable<any>{
        return this.http.post('http://localhost:8000/user/',user,{observe:'response'})
    }
}