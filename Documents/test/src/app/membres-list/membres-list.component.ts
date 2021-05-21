import { Component, OnInit, Input } from '@angular/core';
import {Observable} from 'rxjs';

import {Membre} from '../membre';
import {MembreService} from '../membre.service';

@Component({
  selector: 'membres-list',
  templateUrl: './membres-list.component.html',
  styleUrls: ['./membres-list.component.scss']
})

export class MembresListComponent implements OnInit {
  
  membres: Observable<Membre[]>;

  constructor(private membreService: MembreService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.membres = this.membreService.getMembreList();
  }

}
