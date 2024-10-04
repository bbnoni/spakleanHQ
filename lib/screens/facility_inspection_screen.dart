import 'package:flutter/material.dart';

class FacilityInspectionScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Facility Inspection'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: GridView.count(
          crossAxisCount: 2,
          crossAxisSpacing: 8.0,
          mainAxisSpacing: 8.0,
          children: <Widget>[
            _buildInspectionTile(context, 'Low Traffic Areas\nYellow Zone',
                Colors.yellow, Icons.traffic),
            _buildInspectionTile(context, 'Heavy Traffic Areas\nOrange Zones',
                Colors.orange, Icons.directions_car),
            _buildInspectionTile(context, 'Food Service Areas\nGreen Zone',
                Colors.green, Icons.fastfood),
            _buildInspectionTile(context, 'High Microbial Areas\nRed Zone',
                Colors.red, Icons.warning),
            _buildInspectionTile(context, 'Outdoors & Exteriors\nBlack Zone',
                Colors.black, Icons.park),
            _buildInspectionTile(context, 'Inspection Reports', Colors.white,
                Icons.report, Colors.black),
          ],
        ),
      ),
    );
  }

  Widget _buildInspectionTile(
      BuildContext context, String title, Color bgColor, IconData icon,
      [Color textColor = Colors.white]) {
    return Container(
      padding: EdgeInsets.all(16.0),
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: BorderRadius.circular(8.0),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Icon(icon, size: 50, color: textColor),
          SizedBox(height: 10),
          Text(
            title,
            textAlign: TextAlign.center,
            style: TextStyle(
                fontSize: 18, fontWeight: FontWeight.bold, color: textColor),
          ),
        ],
      ),
    );
  }
}
