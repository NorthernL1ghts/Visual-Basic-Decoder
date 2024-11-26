import os

class VisualBasicExtensionDecoder:
    def __init__(self):
        # Private member variable to store encoded data
        self.m_EncodedData = None

    def SetEncodedData(self, encodedData: str):
        """
        Sets the encoded data to be decoded.
        :param encodedData: The encoded string to decode.
        """
        self.m_EncodedData = encodedData

    def Decode(self) -> str:
        """
        Decodes the encoded data.
        :return: The decoded data as a string.
        """
        if self.m_EncodedData is None:
            raise ValueError("Encoded data is not set.")
        
        # Sample decoding: reversing the encoded data
        decodedData = self.m_EncodedData[::-1]
        
        return decodedData

    def GetDecodedData(self) -> str:
        """
        Returns the decoded data.
        :return: The decoded string.
        """
        if self.m_EncodedData is None:
            raise ValueError("Encoded data is not set.")
        
        return self.Decode()

    def EncodeDataToFile(self, filePath: str):
        """
        Encodes the data and writes it to a file.
        :param filePath: Path of the file to save the encoded data.
        """
        # Create the '../data/' folder if it doesn't exist
        if not os.path.exists('../data'):
            os.makedirs('../data')

        with open(filePath, 'w') as file:
            encodedData = self.m_EncodedData[::-1]  # Example encoding (reverse the data)
            file.write(encodedData)

    def DecodeFileToFile(self, inputFilePath: str, outputFilePath: str):
        """
        Reads encoded data from a file, decodes it, and writes the decoded data to an output file.
        :param inputFilePath: Path to the encoded file.
        :param outputFilePath: Path to save the decoded file.
        """
        # Create the '../out/' folder if it doesn't exist
        if not os.path.exists('../out'):
            os.makedirs('../out')

        # Read encoded data from the file
        with open(inputFilePath, 'r') as file:
            encodedData = file.read()
        
        # Set the encoded data and decode it
        self.SetEncodedData(encodedData)
        decodedData = self.GetDecodedData()
        
        # Write the decoded data to an output file
        with open(outputFilePath, 'w') as file:
            file.write(decodedData)

# Example Usage
if __name__ == "__main__":
    # Creating an instance of the VisualBasicExtensionDecoder
    decoder = VisualBasicExtensionDecoder()
    
    # Set the original data
    originalData = "This is some sample data."
    decoder.SetEncodedData(originalData)
    
    # Encode the data and save it to the "../data/" folder
    decoder.EncodeDataToFile('../data/encoded_file.txt')
    print("Encoded data saved in '../data/encoded_file.txt'.")
    
    # Decode the data from the "../data/" folder and save it to the "../out/" folder
    decoder.DecodeFileToFile('../data/encoded_file.txt', '../out/decoded_file.txt')
    print("Decoded data saved in '../out/decoded_file.txt'.")
