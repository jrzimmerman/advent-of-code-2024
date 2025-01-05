import fs from "node:fs";
import path from "node:path";

export function readFile(filePath = import.meta.dirname, inputName = "input.txt") {
  let file;
  try {
    const inputPath = path.resolve(filePath, inputName);
    file = fs.readFileSync(inputPath, "utf8");
  } catch (error) {
    console.error(error);
  }

  return file;
}
