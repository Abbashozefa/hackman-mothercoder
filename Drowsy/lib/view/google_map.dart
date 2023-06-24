import 'package:flutter/material.dart';
//import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:flutter_map/flutter_map.dart';
//import 'package:latlong/latlong.dart';
import 'package:latlong2/latlong.dart';

class MapScreen extends StatelessWidget {
  final double latitude;
  final double longitude;

  MapScreen({required this.latitude, required this.longitude});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Location'),
      ),
      body: FlutterMap(
        options: MapOptions(
          center: LatLng(latitude, longitude),

          zoom: 12,
        ),
        layers: [
          TileLayerOptions(
            urlTemplate: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            subdomains: ['a', 'b', 'c'],
          ),
          MarkerLayerOptions(
            markers: [
              Marker(
                width: 40,
                height: 40,
                point: LatLng( 12.972442, 77.580643),
                builder: (ctx) => Container(
                  child: Icon(Icons.location_on, color: Colors.red),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
