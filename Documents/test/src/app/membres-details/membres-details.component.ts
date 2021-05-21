import { Component, OnInit, Input} from '@angular/core';
import { Membre } from '../membre';
import { MembreService } from '../membre.service';
import { MembresListComponent } from '../membres-list/membres-list.component';

@Component({
  selector: 'membres-details',
  templateUrl: './membres-details.component.html',
  styleUrls: ['./membres-details.component.scss']
})
export class MembresDetailsComponent implements OnInit {

  @Input() id: number;
  @Input() membre: Membre = null;
  urlImage: string = "http://127.0.0.1:8000"

  constructor(private membreService: MembreService) { }

  ngOnInit(): void {
    if(this.membre == null){
      this.reloadData();
    }
  }

  reloadData(){
    this.membreService.getMembreById(this.id).subscribe(
      data => {
        this.membre = data;
        this.urlImage = this.urlImage+this.membre.photo;
      }
    )
  }
}
