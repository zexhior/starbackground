import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { MembresListComponent } from './membres-list/membres-list.component';
import { NumeroDetailsComponent } from './numero-details/numero-details.component';
import { MembresDetailsComponent } from './membres-details/membres-details.component';
import { CategorieDetailsComponent } from './categorie-details/categorie-details.component';
import { FbDetailsComponent } from './fb-details/fb-details.component';
import { MailDetailsComponent } from './mail-details/mail-details.component';
import { ActiviteDetailsComponent } from './activite-details/activite-details.component';
import { DescriptionDetailsComponent } from './description-details/description-details.component';
import { PhotoDetailsComponent } from './photo-details/photo-details.component';
import { PresenceDetailsComponent } from './presence-details/presence-details.component';
import { PresencesListComponent } from './presences-list/presences-list.component';
import { ActivitesListComponent } from './activites-list/activites-list.component';
import { UploadFileComponent } from './upload-file/upload-file.component';

@NgModule({
  declarations: [
    AppComponent,
    MembresListComponent,
    NumeroDetailsComponent,
    FbDetailsComponent,
    MailDetailsComponent,
    MembresDetailsComponent,
    CategorieDetailsComponent,
    ActiviteDetailsComponent,
    ActivitesListComponent,
    DescriptionDetailsComponent,
    PhotoDetailsComponent,
    PresenceDetailsComponent,
    PresencesListComponent,
    UploadFileComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
