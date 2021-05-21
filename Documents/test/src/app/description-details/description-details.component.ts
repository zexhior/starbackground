import { Component, Input, OnInit } from '@angular/core';
import { ActiviteService } from '../activite.service';
import { Description } from '../description';

@Component({
  selector: 'description-details',
  templateUrl: './description-details.component.html',
  styleUrls: ['./description-details.component.scss']
})
export class DescriptionDetailsComponent implements OnInit {

  @Input() id: number;
  paragraphe: Description;

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.activiteService.getDescriptionById(this.id).subscribe(
      data => {
        this.paragraphe = data;
      }
    );
  }
}
