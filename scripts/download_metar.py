#!/usr/bin/env python3
"""
METAR Data Downloader

This script downloads METAR data from aviationweather.gov, decompresses it,
and stores it in a timestamped directory structure.
"""

import os
import sys
import gzip
import requests
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
from pathlib import Path

# Configuration
METAR_URL = "https://aviationweather.gov/data/cache/metars.cache.xml.gz"
BASE_DATA_DIR = "data"

def create_timestamp_directory():
    """Create a directory structure based on current UTC timestamp."""
    now = datetime.now(timezone.utc)
    
    # Format: data/2025/09/12/14-30 (year/month/day/hour-minute)
    dir_path = Path(BASE_DATA_DIR) / str(now.year) / f"{now.month:02d}" / f"{now.day:02d}" / f"{now.hour:02d}-{now.minute:02d}"
    
    # Create directory if it doesn't exist
    dir_path.mkdir(parents=True, exist_ok=True)
    
    return dir_path, now

def download_and_decompress(url):
    """Download and decompress the METAR data file."""
    try:
        print(f"Downloading METAR data from {url}")
        
        # Download the gzipped file
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Decompress the gzip content
        print("Decompressing data...")
        xml_content = gzip.decompress(response.content)
        
        return xml_content
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error decompressing data: {e}")
        sys.exit(1)

def validate_xml(xml_content):
    """Validate that the XML content is well-formed."""
    try:
        ET.fromstring(xml_content)
        return True
    except ET.ParseError as e:
        print(f"XML validation error: {e}")
        return False

def save_xml_data(xml_content, directory_path, timestamp):
    """Save the XML content to a file."""
    # Create filename with timestamp
    filename = f"metars_{timestamp.strftime('%Y%m%d_%H%M')}UTC.xml"
    file_path = directory_path / filename
    
    # Validate XML before saving
    if not validate_xml(xml_content):
        print("Warning: XML content appears to be malformed")
    
    # Save the XML content
    try:
        with open(file_path, 'wb') as f:
            f.write(xml_content)
        print(f"Successfully saved METAR data to {file_path}")
        
        # Create a metadata file with download info
        metadata_path = directory_path / "download_info.txt"
        with open(metadata_path, 'w') as f:
            f.write(f"Download timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
            f.write(f"Source URL: {METAR_URL}\n")
            f.write(f"File size: {len(xml_content)} bytes\n")
            f.write(f"XML filename: {filename}\n")
        
        return file_path
        
    except IOError as e:
        print(f"Error saving file: {e}")
        sys.exit(1)

def main():
    """Main function to orchestrate the download and storage process."""
    print("Starting METAR data download process...")
    
    # Create timestamped directory
    directory_path, timestamp = create_timestamp_directory()
    print(f"Created directory: {directory_path}")
    
    # Download and decompress data
    xml_content = download_and_decompress(METAR_URL)
    
    # Save the data
    saved_file = save_xml_data(xml_content, directory_path, timestamp)
    
    print(f"METAR data processing completed successfully!")
    print(f"Data saved to: {saved_file}")

if __name__ == "__main__":
    main()
