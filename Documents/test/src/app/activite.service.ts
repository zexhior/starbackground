import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ActiviteService {
  baseUrl = "http://127.0.0.1:8000/api"

  constructor(private http: HttpClient) { }

  getCategorieById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/categories/${id}`);
  }

  getCategorieList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/categories/`);
  }

  getActiviteById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/activites/${id}`);
  }

  getActiviteList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/activites/`);
  }

  getDescriptionById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/descriptions/${id}`);
  }

  getDescriptionList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/descriptions/`);
  }

  getPhotoById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/photos/${id}`);
  }

  getPhotoList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/photos/`);
  }

  getPresenceById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/presences/${id}`);
  }

  getPresencesList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/presences/`);
  }
}
