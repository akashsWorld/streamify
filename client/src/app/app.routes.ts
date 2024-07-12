import { Routes } from '@angular/router';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { ChannelComponent } from './pages/channel/channel.component';
import { AuthComponent } from './pages/auth/auth.component';
import { SignInComponent } from './pages/sign-in/sign-in.component';
import { SignUpComponent } from './pages/sign-up/sign-up.component';
import { CreateChannelComponent } from './pages/create-channel/create-channel.component';
import { VideosComponent } from './pages/videos/videos.component';
import { ErrorComponent } from './pages/error/error.component';

export const routes: Routes = [
    {
        path:'',
        component:HomePageComponent,
        pathMatch:'full',
        children:[
            {
                path:'',
                component:VideosComponent,
                pathMatch:'full',
            },
            {
                path:'channel/:id',
                component:ChannelComponent
            },
            {
                path:'createChannel',
                component:CreateChannelComponent
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
    },
    {
        path:'error-occured',
        component:ErrorComponent
    }
    
];
