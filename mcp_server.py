from fastmcp import FastMCP

# 1. 서버 인스턴스 생성
mcp = FastMCP("add-mcp-http")

# 2. @mcp.tool 데코레이터로 함수를 '도구'로 등록
@mcp.tool
def add(a: int, b: int) -> int:
    """두 숫자를 더합니다."""
    return a + b

# 3. 서버 실행 (스크립트가 직접 실행될 때만)
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000 )