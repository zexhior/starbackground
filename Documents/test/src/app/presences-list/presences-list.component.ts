import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ActiviteService } from '../activite.service';
import { Presence } from '../presence';

@Component({
  selector: 'presences-list',
  templateUrl: './presences-list.component.html',
  styleUrls: ['./presences-list.component.scss']
})

export class PresencesListComponent implements OnInit {
  
  presences: Observable<Presence[]>

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.presences = this.activiteService.getPresencesList();
  }

}
