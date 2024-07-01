import { Routes } from '@angular/router';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { ChannelComponent } from './pages/channel/channel.component';
import { AuthComponent } from './pages/auth/auth.component';
import { SignInComponent } from './pages/sign-in/sign-in.component';
import { SignUpComponent } from './pages/sign-up/sign-up.component';

export const routes: Routes = [
    {
        path:'',
        component:HomePageComponent,
        children:[
            {
                path:'channel',
                component:ChannelComponent
            }
        ]
    },
    {
        path:'auth',
        component:AuthComponent,
        children:[
            {
                path:'',
                component:SignInComponent
            },
            {
                path:'signUp',
                component:SignUpComponent
            }
        ]
    }
    
];
