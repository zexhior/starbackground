import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EnvoifichierService {
  baseUrl: string = " ";

  constructor(private http: HttpClient) { }

  envoiFichier(fichierAEnvoyer: File): Observable<any>{
    const formData: FormData = new FormData();
    formData.append('fichier', fichierAEnvoyer, fichierAEnvoyer.name);
    return this.http.post(
      this.baseUrl,
      formData);
  }
}
