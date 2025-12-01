import os
import logging
from datetime import datetime
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class CoreEngine:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.initialize()

    def initialize(self):
        """Initialize the core engine with necessary setup."""
        logger.info("Initializing Core Engine...")
        self.start_time = datetime.now()
        self.status = "READY"

    def process_data(self, data: List) -> Dict:
        """Process the given data and return results."""
        logger.info("Processing data...")
        if not data:
            logger.warning("No data provided for processing.")
            return {}

        results = {}
        for item in data:
            try:
                processed_item = self._process_item(item)
                results[item] = processed_item
            except Exception as e:
                logger.error(f"Error processing item {item}: {e}")

        logger.info("Data processing completed.")
        return results

    def _process_item(self, item: str) -> str:
        """Process a single item."""
        return item.upper()

    def shutdown(self):
        """Shutdown the core engine and clean up resources."""
        logger.info("Shutting down Core Engine...")
        self.status = "SHUTDOWN"
        logger.info(f"Engine ran for {datetime.now() - self.start_time}")

def main():
    engine = CoreEngine()
    data = ["example1", "example2", "example3"]
    results = engine.process_data(data)
    logger.info(f"Processing results: {results}")
    engine.shutdown()

if __name__ == "__main__":
    main()