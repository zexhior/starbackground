import { Component, Input, OnInit } from '@angular/core';
import { ActiviteService } from '../activite.service';
import { Presence } from '../presence';

@Component({
  selector: 'presence-details',
  templateUrl: './presence-details.component.html',
  styleUrls: ['./presence-details.component.scss']
})
export class PresenceDetailsComponent implements OnInit {

  @Input() presence: Presence;

  constructor() { }

  ngOnInit(): void {
  }
}
