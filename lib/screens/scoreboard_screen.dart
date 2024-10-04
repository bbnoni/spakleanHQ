import 'package:flutter/material.dart';

import 'facility_inspection_screen.dart';

class ScoreboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Scoreboard - Spaklean'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: GridView.count(
          crossAxisCount: 2,
          crossAxisSpacing: 8.0,
          mainAxisSpacing: 8.0,
          children: <Widget>[
            _buildGridTile(
              context,
              'Facility Inspection',
              Icons.cleaning_services,
              Colors.blue,
              FacilityInspectionScreen(),
            ),
            _buildGridTile(
                context, 'Task Compliance', Icons.task_alt, Colors.green, null),
            _buildGridTile(context, 'Tools & Equipment Audit (TEA)',
                Icons.build, Colors.orange, null),
            _buildGridTile(
                context, 'Safety Records', Icons.security, Colors.red, null),
            _buildGridTile(context, 'Custodian Records', Icons.person,
                Colors.purple, null),
            _buildGridTile(
                context, 'Cleaning Times', Icons.timer, Colors.cyan, null),
            _buildGridTile(context, 'Notification', Icons.notifications,
                Colors.amber, null),
            _buildGridTile(context, 'Setup', Icons.settings, Colors.grey, null),
          ],
        ),
      ),
    );
  }

  Widget _buildGridTile(BuildContext context, String title, IconData icon,
      Color color, Widget? nextPage) {
    return GestureDetector(
      onTap: () {
        if (nextPage != null) {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => nextPage),
          );
        }
      },
      child: Container(
        padding: EdgeInsets.all(16.0),
        decoration: BoxDecoration(
          color: color.withOpacity(0.2),
          borderRadius: BorderRadius.circular(8.0),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Icon(icon, size: 50, color: color),
            SizedBox(height: 10),
            Text(
              title,
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
