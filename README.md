HeartRate
=========

Parses Google My Tracks data files to look at heart rate data

This reads the csv output format for My Tracks, and can read multiple files and plot them on a graph.

The settings for the code come from a json *.settings* file. *file_path* indicates the directory where csv export files are located, and *type* indicates the type of activity for the recording (e.g. walking, running, cycling).

```
{
  "file_path": "Directory to csv files"
  "type": "type of csv file here"
}
```
